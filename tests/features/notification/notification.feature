Feature: Implementar o endpoint para receber notificação de mudança de preço e estoque
  Seller hospedado na VTEX vai chamar endpoint do Marketplace. Toda vez que o SKU mudar o preço e ou o estoque no Seller,
  o Seller tem que chamar esse endpoint do Marketplace, simplesmente comunicando a mudança. Ao receber esse request o
  Marketplace vem buscar o preço e estoque no Seller no metodo de consulta politica comercial.

  Scenario: Notifica o Marketplace Não VTEX que houve uma mudança nas condições comerciais de uma SKU

    Given que eu altero o preço de um SKU em "https://loja.vtex.com/api/sku/123" para o valor de "999"
      And o Seller manda uma notificação para "https://mplace.com/api/notification" comunicando a mudança do preço do SKU
      And o Marketplace faz a solicitação "https://loja.vtex.com/api/sku/123" para saber o novo preço do SKU
      And o Marketplace grava o novo preço do SKU em sua base de dados
     Then o novo preço do SKU fica disponível em "https://mplace.com/api/products/1/"
