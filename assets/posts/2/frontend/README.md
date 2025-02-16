# Frontend

## Contribution

Please install [NodeJS](https://nodejs.org/).

Please install VSCode extensions:

- Auto Rename Tag
- ES7+ React/Redux/React-Native snippets
- ESLint
- Highlight Matching Tag
- Prettier - Code formatter

To install dependencies, from `./frontend` folder run the command:

```bash
npm install
```

To update dependencies, from `./frontend` folder run the command:

```bash
npm update --save
```

To start implementing you need to run the development server:

```bash
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) with your browser to see the result.

To generate a distributable frontend for serving by the backend:

```bash
npm run build
```

Backend utilizes /api and /docs. Ensure frontend development does not impact these paths.

## Backend endpoints

To generate TypeScript endpoint definitions from the backend OpenAPI:

```bash
npx openapi-typescript http://localhost:8080/docs/docs.yaml --output ./src/services/backend/endpoints.d.ts
```
