import React, { BrowserRouter, Route, Routes } from "react-router-dom";

//importando todas as páginas
import { Home } from "../pages";
import { NoPage } from "../pages";
import { Marca } from "../pages";

//importando todas as paginas que foram exportadas no ../pages/index.ts

const Router = () => (
  //constante Router é igual a uma função vazia que vai executar a pesquisa rotas e paginas
  <BrowserRouter>
    <Routes>
      <Route index element={<Home />} />
      <Route path="/home" element={<Home />} />
      <Route path="/marca" element={<Marca />} />
      <Route path="*" element={<NoPage />} />
    </Routes>
  </BrowserRouter>
);

export default Router;
