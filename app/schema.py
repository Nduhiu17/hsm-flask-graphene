import graphene
from flask_graphql_auth import create_access_token, create_refresh_token, mutation_jwt_required, AuthInfoField, \
    query_header_jwt_required, mutation_jwt_refresh_token_required, get_jwt_identity
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from app.models.user_model import User as UserModel, Store as StoreModel, User, Store


class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (graphene.relay.Node,)


class StoreObject(SQLAlchemyObjectType):
    class Meta:
        model = StoreModel
        interfaces = (graphene.relay.Node,)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserObject)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = User.query.filter_by(username=username).first()
        if user:
            return CreateUser(user=user)
        user = User(username=username, password=password, email=email)
        if user:
            User.save(user)
        return CreateUser(user=user)


class AuthMutation(graphene.Mutation):
    access_token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String()
        password = graphene.String()

    def mutate(self, info, username, password):
        user = User.query.filter_by(username=username, password=password).first()
        print(user)
        if not user:
            raise Exception('Authenication Failure : User is not registered')
        return AuthMutation(
            access_token=create_access_token(username),
            refresh_token=create_refresh_token(username)
        )


class ProtectedStore(graphene.Union):
    class Meta:
        types = (StoreObject, AuthInfoField)


class CreateStore(graphene.Mutation):
    store = graphene.Field(ProtectedStore)

    class Arguments:
        name = graphene.String(required=True)
        user_id = graphene.Int(required=True)
        token = graphene.String()

    @mutation_jwt_required
    def mutate(self, info, name, user_id):
        store = Store(name=name, user_id=user_id)
        if store:
            Store.save(store)
        return CreateStore(store=store)


class RefreshMutation(graphene.Mutation):
    class Arguments(object):
        refresh_token = graphene.String()

    new_token = graphene.String()

    @mutation_jwt_refresh_token_required
    def mutate(self):
        current_user = get_jwt_identity()
        return RefreshMutation(new_token=create_access_token(identity=current_user))


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    auth = AuthMutation.Field()
    protected_create_store = CreateStore.Field()
    refresh = RefreshMutation.Field()  ## this is added


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_users = SQLAlchemyConnectionField(UserObject)
    all_stores = SQLAlchemyConnectionField(StoreObject)
    get_store = graphene.Field(type=ProtectedStore, token=graphene.String(), id=graphene.Int())

    @query_header_jwt_required
    def resolve_get_store(self, info, id):
        store = Store.find_by_id(soreid=id)
        return store


schema = graphene.Schema(query=Query, mutation=Mutation)
