#Primeiramente será usado um comando que mostre a minha localização atual, ou seja, a pasta ou o diretório onde estou 
pwd
#Para que seja possível visualizar os comandos é necessário mudar as permissões de um arquivo ou pasta no terminal 
#Para isso, basta rodar o seguinte comando: chmod +x bash_cript.sh
#Após isso, é necessário adicionar o comando: ./bash_script.sh

#Em seguida, deseja-se gerar uma lista com detalhes do conteúdo da minha pasta
ls -l #Tal comando irá gerar uma lista larga dos arquivos na pasta e, além disso, irá exibir as permissões

#Posteriormente, essa lista de arquivos serão redirecionados para um novo arquivo de texto (lista_HOME.txt) 
ls -l > lista_HOME.txt 
#Para verificar se tudo ocorreu bem basta adicionar o seguinte comando no terminal: nano lista_HOME.txt 

#Por último, deseja-se saber o data atual e, para isso, será inserido um comando que imprima a data atual
date
