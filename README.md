# 🛠️ Automação de Cadastro de Produtos com PyAutoGUI

Este projeto utiliza **PyAutoGUI** para automatizar o processo de cadastro de produtos. A automação interage diretamente com o navegador, preenchendo formulários de maneira repetitiva, economizando tempo e esforço em processos manuais.

## 📋 Funcionalidades

O script realiza as seguintes operações de forma automatizada:

1. **Abertura do Navegador**: Inicia o Google Chrome automaticamente.
2. **Navegação até o site**: Digita a URL do site de login na barra de endereços e pressiona enter.
3. **Login Automático**: Preenche o e-mail e senha para efetuar o login no site.
4. **Importação de Dados**: Carrega os produtos a serem cadastrados a partir de um arquivo CSV.
5. **Cadastro de Produtos**: Preenche os campos do formulário de cadastro (código, marca, tipo, categoria, preço, custo, observação) e envia o formulário para cada produto.
6. **Repetição do Processo**: Realiza o cadastro de todos os produtos presentes no arquivo CSV até que todos sejam submetidos.

## 🚀 Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal usada no projeto.
- **PyAutoGUI**: Biblioteca para automação de interações com a interface gráfica, como clicar e digitar.
- **Pandas**: Usada para carregar e manipular a base de dados dos produtos.
- **Time**: Módulo nativo do Python para introduzir atrasos e controlar o tempo de execução.


## 📦 Pré-requisitos

Antes de rodar o projeto, você precisará ter instalado em sua máquina:

- **Python 3.x**
- **PyAutoGUI** e **Pandas**

### Instalando dependências

Execute os seguintes comandos para instalar as dependências:

```bash
pip install pyautogui pandas
