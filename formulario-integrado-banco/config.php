<?php 

    $dbHost = 'Localhost';
    $dbUsername = 'root';
    $dbPassword = '';
    $dbName = 'formulario-dev-gabriel';

    $conexao = new mysqli($dbHost,$dbUsername,$dbPassword,$dbName);

    /*
    === Para testar conexão com o banco de dados ===

    if($conexao->connect_errno){
        echo "Erro";
    }else{
        echo "Sucesso!";
    }
    */

?>