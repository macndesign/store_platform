# coding: utf-8
from __future__ import unicode_literals, absolute_import
from lettuce import step


@step(u'Given que eu altero o preço de um SKU em "([^"]*)" para o valor de "([^"]*)"')
def given_que_eu_altero_o_preco_de_um_sku_em_group1_para_o_valor_de_group2(step, group1, group2):
    assert False, 'This step must be implemented'


@step(u'And o Seller manda uma notificação para "([^"]*)" comunicando a mudança do preço do SKU')
def and_o_seller_manda_uma_notificacao_para_group1_comunicando_a_mudanca_do_preco_do_sku(step, group1):
    assert False, 'This step must be implemented'


@step(u'And o Marketplace faz a solicitação "([^"]*)" para saber o novo preço do SKU')
def and_o_marketplace_faz_a_solicitacao_group1_para_saber_o_novo_preco_do_sku(step, group1):
    assert False, 'This step must be implemented'


@step(u'And o Marketplace grava o novo preço do SKU em sua base de dados')
def and_o_marketplace_grava_o_novo_preco_do_sku_em_sua_base_de_dados(step):
    assert False, 'This step must be implemented'


@step(u'Then o novo preço do SKU fica disponível em "([^"]*)"')
def then_o_novo_preco_do_sku_fica_disponivel_em_group1(step, group1):
    assert False, 'This step must be implemented'
