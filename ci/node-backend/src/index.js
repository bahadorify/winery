require('dotenv').config();
import express from 'express';
import { ApolloServer } from 'apollo-server-express';
import mongoose from 'mongoose';
import { typeDefs } from './typeDefs';
import { resolvers } from './resolvers';

const { MONGO_PASSWORD, MONGO_HOST, BACKEND_PORT } = process.env;

const startServer = async () => {
  const app = express();

  const server = new ApolloServer({
    typeDefs,
    resolvers
  });

  server.applyMiddleware({ app });

  console.log(MONGO_PASSWORD, MONGO_HOST, BACKEND_PORT);
  await mongoose.connect(
    `mongodb://root:${MONGO_PASSWORD}@${MONGO_HOST}:27017/wines?authSource=admin`,
    {
      useNewUrlParser: true,
      useUnifiedTopology: true
    }
  );

  const port = BACKEND_PORT || 4000;
  console.log(process.env);
  app.listen({ port }, () =>
    console.log(
      `🚀 Server ready at http://localhost:${port}${server.graphqlPath}`
    )
  );
};

startServer();
