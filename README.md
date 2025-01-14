# Automação de Cadastro de Produtos 🛒

Este projeto foi desenvolvido para automatizar o processo de cadastro de produtos no sistema de gestão da empresa. A automação utiliza Python e bibliotecas específicas para interações com a interface gráfica e manipulação de dados. Com isso, o cadastro de milhares de produtos, que antes era feito manualmente, agora pode ser realizado de forma automática, reduzindo o tempo e minimizando erros humanos.

## 🚀 Funcionalidades

- Abertura automática do sistema no navegador.
- Login automatizado com credenciais previamente configuradas.
- Leitura de uma base de dados em formato CSV contendo informações dos produtos.
- Preenchimento automático de formulários no sistema.
- Execução diária ou sob demanda.

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**: Linguagem principal utilizada no desenvolvimento.
- **Bibliotecas**:
  - `pyautogui`: Para automação de interações com a interface gráfica (movimento do mouse, cliques, teclas, etc.).
  - `pandas`: Para manipulação e leitura de dados em arquivos CSV.
  - `time`: Para gerenciar intervalos de espera e garantir que o sistema acompanhe a automação.
  - `openpyxl`: Para lidar com arquivos no formato Excel (se necessário para futuras implementações).

## 📂 Estrutura do Projeto
├── main.py                # Script principal com a lógica da automação <br/>
├── produtos.csv           # Arquivo CSV contendo os dados dos produtos (código, marca, tipo, categoria, etc.)<br/>
└── README.md              # Documentação do projeto

## 📋 Pré-requisitos

1. Ter o Python 3.12 ou superior instalado.
2. Instalar as bibliotecas necessárias:
   ```bash
   pip install pyautogui pandas openpyxl

## 🖥️ Como Utilizar

1. Clone este repositório:
   git clone [https://github.com/seuusuario/automacao-cadastro-produtos.git](https://github.com/saints-cloud/Automacao-de-tarefas)

2. Navegue até o diretório do projeto:
   cd automacao-cadastro-produtos

3. Execute o script principal:
   python main.py


## 📌 Detalhes do Script

1. **Abertura do Sistema**:
   - O script utiliza o pyautogui para abrir o navegador, acessar o sistema e realizar o login automaticamente.

2. **Leitura da Base de Dados**:
   - Utiliza pandas para carregar os dados do arquivo produtos.csv, que deve conter colunas como codigo, marca, tipo, categoria, preco_unitario, custo e obs.

3. **Cadastro dos Produtos**:
   - Para cada linha da base de dados, o script preenche os campos do sistema e conclui o cadastro antes de avançar para o próximo produto.

---

## ⚠️ Considerações Importantes

- Certifique-se de que a resolução do monitor e as coordenadas utilizadas no pyautogui estão configuradas corretamente.
- Ajuste os tempos de espera (time.sleep) conforme a velocidade do seu sistema e da conexão com a internet.
- Use com responsabilidade, respeitando as políticas do sistema e da empresa.

---

## 📧 Contato

Caso tenha dúvidas ou sugestões, entre em contato:
- Nome: Lays Pinheiro
- Email: [pinheiro.lays01@gmail.com](mailto:seuemail@gmail.com)
- LinkedIn: [[LinkedIn](https://www.linkedin.com/in/laysspinheiro/)]
