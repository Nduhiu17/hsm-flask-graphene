#!/usr/bin/env bash
import pytest
from flask_graphql import GraphQLView
from flask_graphql_auth import GraphQLAuth
from flask_migrate import MigrateCommand
from flask_script import Manager, Server
from app import create_app, db
from app.schema import schema

app = create_app()
auth = GraphQLAuth(app)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)
manager = Manager(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command('server', Server)

if __name__ == '__main__':
    manager.run()
