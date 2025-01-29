# Fluxo_Caixa_GCP
Solução para fluxo de caixa utilizando nuvem do Google

Instruções para Execução Local
1. Clonar o repositório

bash
git clone https://github.com/seu-usuario/carrefour-solution.git
cd carrefour-solution

2. Configuração do ambiente local (Docker)
Certifique-se de ter o Docker e o Docker Compose instalados
Execute o comando a seguir para inicializar o ambiente de desenvolvimento local com Docker Compose:
bash
docker-compose up --build
Isso irá inicializar os microsserviços (Lançamento de Valores, Atualização de Saldo, Geração de Relatórios) e o banco de dados SQL Server em containers.


3. Executando os microsserviços
O serviço de Lançamento de Valores estará disponível em http://localhost:5000/launch para registrar lançamentos.
O serviço de Geração de Relatórios estará disponível em http://localhost:5001/generate_report para gerar relatórios.

4. Acessando o banco de dados SQL Server
Você pode acessar o SQL Server em localhost:1433 com o usuário sa e a senha YourPassword123.

5.Parar os containers
Quando terminar, basta parar os containers com o comando:
docker-compose down

