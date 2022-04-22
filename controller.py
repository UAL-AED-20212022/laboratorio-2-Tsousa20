from models.LinkedList import LinkedList

def inserir_pais_inicio(lista_paises, pais_novo):
    lista_paises.insert_at_start(pais_novo)
    return lista_paises

def inserir_pais_fim(lista_paises, pais_novo):
    lista_paises.insert_at_end(pais_novo)
    return lista_paises

def inserir_pais_depois_elemento(lista_paises, pais_novo, pais_registado):
    lista_paises.insert_after_item(pais_registado, pais_novo)
    return lista_paises

def inserir_pais_antes_elemento(lista_paises, pais_novo, pais_registado):
    lista_paises.insert_before_item(pais_registado, pais_novo)
    return lista_paises

def inserir_pais_indice(lista_paises, pais_novo, indice):
    lista_paises.insert_at_index(indice, pais_novo)
    return lista_paises

def verificar_numero_elementos(lista_paises):
    lista_paises.get_count()
    return lista_paises

def verificar_pais(lista_paises, pais):
    lista_paises.search_item(pais)
    return lista_paises

def eliminar_primeiro_elemento(lista_paises):
    lista_paises.delete_at_start()
    return lista_paises

def eliminar_ultimo_elemento(lista_paises):
    lista_paises.delete_at_end()
    return lista_paises

def eliminar_determinado_elemento(lista_paises, pais):
    lista_paises.delete_element_by_value(pais)
    return lista_paises