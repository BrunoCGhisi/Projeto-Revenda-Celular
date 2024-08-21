import React, { useState, useEffect } from "react";
import { BranchVO } from "../services/types";
import axios from "axios";

import {
    Accordion,
    AccordionDetails,
    Box,
    Modal,
    AccordionSummary,
    Button,
    Divider,
    IconButton,
    Stack,
    TextField,
    Typography,
  } from "@mui/material";

import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";
import DeleteIcon from "@mui/icons-material/Delete";
import EditIcon from "@mui/icons-material/Edit";
import DoneIcon from "@mui/icons-material/Done";

 const Marca = () => {
    const [branchs, setBranchs] = useState<BranchVO[]>([]);
    const [branchId, setBranchId] = useState("")

    const [nome, setNome] = useState("");

    async function getBranch() {
        try {
          const response = await axios.get("http://localhost:3000/categoria");
          setBranchs(response.data.marca); // aqui pe o nome que vem do back antona burra
        } catch (error: any) {
          new Error(error);
        }
      }

      async function postBranch() {
        try {
          const response = await axios.post("http://localhost:3000/autor", {
            nome: nome,
          });
          getBranch();
          if (response.status === 200) alert("Marca cadastra com sucesso!");
        } catch (error: any) {
          new Error(error);
        } finally {
          
        }
      }

      async function putBranch() {
        try {
          const response = await axios.put(
            `http://localhost:3000/autor?id=${branchId}`,
            {
              nome: nome,
            }
          );
          if (response.status === 200) alert("Autor atualizado com sucesso!");
          getBranch();
        } catch (error: any) {
          new Error(error);
        } finally {

        }
      }

      async function delBranch(id: string) {
        try {
          const response = await axios.delete(
            `http://localhost:3000/autor?id=${branchId}`
          );
          if (response.status === 200) alert("Marca deletado com sucesso!");
          getBranch();
        } catch (error: any) {
          new Error(error);
        } finally {

        }
      }
  //------------------------------------------------------

  useEffect(() => {
    getBranch();
  }, []);

  //------------------------------------------------------     
  
  return (
    <Box>
      <Typography id="modal-modal-title" variant="h6" component="h2">
        Novo Cliente
      </Typography>

      <TextField //Prencher Categoria
        id="outlined-helperText"
        label="Nome"
        defaultValue=""
        helperText="Obrigatório"
        value={nome}
        onChange={(e) => setNome(e.target.value)}
      />
      <Button
        onClick={postBranch}
        variant="outlined"
        startIcon={<DoneIcon />}
      >
        Cadastrar
      </Button>

    </Box>
  )
 }

 export default Marca

