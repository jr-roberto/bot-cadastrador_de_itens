
# 🤖 Utilizando o Script para Cadastro de Itens em um Sistema Web 📝



Este script utiliza a biblioteca Selenium para automatizar o processo de cadastro de itens em um sistema web. Através da interação com elementos da página, o script preenche os campos necessários com dados obtidos a partir de um arquivo CSV.


Este script é útil para automatizar o processo de cadastro de itens em um sistema web, economizando tempo e esforço manual. No entanto, é importante ajustar os XPath e os passos do script de acordo com a estrutura e os elementos específicos da página web em que você deseja realizar o cadastro dos itens.


# Aqui está um resumo de como o script funciona:

1. Importação de bibliotecas: O script começa importando as bibliotecas necessárias, incluindo o Selenium, o ChromeDriverManager e o módulo "ler_arquivo_csv" para obter os dados dos itens a serem cadastrados.
2. Configuração do webdriver: O script configura o webdriver do Chrome e inicia uma instância do navegador.
3. Acesso ao sistema web: O script navega até a URL do sistema web que será utilizado para cadastrar os itens.
4. Mapeamento dos elementos da tela: O script define XPath para os elementos da página, como os campos de seleção, campos de texto e botões.
5. Leitura dos itens do arquivo CSV: O script lê os itens a serem cadastrados a partir do arquivo CSV utilizando a função "ler_arquivo_csv".
6. Loop de cadastro: Para cada item na lista de itens a serem cadastrados, o script realiza as seguintes etapas:
   1. Selecionar o grupo: O script encontra o elemento de seleção de grupo na página e seleciona a opção correspondente ao grupo do item atual.
   2. Preencher o código do item: O script encontra o campo de texto do código do item na página e insere o código do item atual.
   3. Preencher a descrição: O script encontra o campo de texto da descrição na página e insere a descrição do item atual.
   4. Preencher o local de estoque: O script encontra o campo de texto do local de estoque na página e insere o local de estoque do item atual.
   5. Preencher o fabricante: O script encontra o campo de texto do fabricante na página e insere o fabricante do item atual.
   6. Selecionar o laudo: O script encontra o elemento de seleção de laudo na página e seleciona a opção correspondente ao laudo do item atual.
   7. Clicar em cadastrar: O script encontra o botão de cadastrar na página e clica nele para enviar o formulário de cadastro.
   8. Finalizar o cadastro: Após o cadastro, o script aguarda a exibição de uma janela popup de confirmação e a fecha clicando no botão correspondente.

Encerramento do script: Após o loop de cadastro, o script exibe uma mensagem de "Finalizado" e aguarda por 3 segundos antes de encerrar o webdriver e fechar o navegador.

https://github.com/jr-roberto/bot-cadastrador_de_itens/assets/91014834/cec1e8ad-84df-4fac-b4e2-0befc627aa54
