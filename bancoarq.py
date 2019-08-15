# coding=utf-8
#Python v3.5
import os
arquivo = open('banco.txt','w')
arquivo.close()
continua = True
while continua:
	print ("------------MENU------------")
	print ("0.Sair")
	print ("1.Cadastrar conta")
	print ("2.Remover conta")
	print ("3.Creditar")
	print ("4.Debitar")
	print ("5.Transferir")
	print ("6.Consultar Saldo\n")
	usuario = int(input("Digite a operação desejada: "))
	if usuario == 0:
		print ("Finalizado com sucesso.")
		continua = False
	elif usuario == 1:
		arquivo = open('banco.txt','r')
		achou = 0
		nova_conta = input("Digite o numero da conta que deseja cadastrar: ")
		for linha in arquivo:
			linhas = linha.split(' ')
			if linhas[0] == nova_conta:
				achou = 1
		if achou == 1:
			print ("Conta já existe. Tente novamente")
			arquivo.close()
		else:
			arquivo = open('banco.txt','a')
			conta = "{0} {1}".format(nova_conta,'0.0\n')
			arquivo.write(conta)
			arquivo.close()
			print ("Conta cadastrada com sucesso!")
	elif usuario == 2:
		arquivo = open('banco.txt','r')
		arquivotemp = open('bancotemp.txt','a')
		achou = 0
		remover_conta = input("Digite o numero da conta que deseja remover: ")
		for linha in arquivo:
			linhas = linha.split(' ')
			if linhas[0] != remover_conta:
				arquivotemp.write(linha)
			else:
				achou = 1
		if achou == 0:
			print ("Conta não existe. Tente novamente.")
			arquivo.close()
			arquivotemp.close()
			os.remove('bancotemp.txt')
		else:
			arquivo = open('banco.txt','w')
			arquivotemp = open('bancotemp.txt','r')
			copia = arquivotemp.read()
			arquivo.write(copia)
			arquivo.close()
			arquivotemp.close()
			os.remove('bancotemp.txt')
			print ("Conta Removida com sucesso!")
	elif usuario == 3:
		arquivo = open('banco.txt','r')
		arquivotemp = open('bancotemp.txt','a')
		achou = 0
		conta = input("Digite o numero da conta que deseja creditar: ")
		for linha in arquivo:
			linhas = linha.split(' ')
			if linhas[0] == conta:
				achou = 1
				saldo = float(linhas[1])
			else:
				arquivotemp.write(linha)
		if achou == 0:
			print ("Conta não existe. Tente novamente.")
			arquivo.close()
			arquivotemp.close()
			os.remove('bancotemp.txt')
		else:
			valor = float(input("Digite o valor do crédito: "))
			if valor <= 0:
				print ("Não é possível creditar valores negativos ou nulos.")
				arquivo.close()
				arquivotemp.close()
				os.remove('bancotemp.txt')
			else:
				arquivo = open('banco.txt','w')
				conta_credito = "{0} {1}\n".format(conta,str(saldo + valor))
				arquivotemp.write(conta_credito)
				arquivotemp = open('bancotemp.txt','r')
				copia = arquivotemp.read()
				arquivo.write(copia)
				arquivo.close()
				arquivotemp.close()
				os.remove('bancotemp.txt')
				print ("Crédito realizado com sucesso!")
	elif usuario == 4:
		arquivo = open('banco.txt','r')
		arquivotemp = open('bancotemp.txt','a')
		achou = 0
		conta = input("Digite o numero da conta que deseja debitar: ")
		for linha in arquivo:
			linhas = linha.split(' ')
			if linhas[0] == conta:
				achou = 1
				saldo = float(linhas[1])
			else:
				arquivotemp.write(linha)
		if achou == 0:
			print ("Conta não existe. Tente novamente.")
			arquivo.close()
			arquivotemp.close()
			os.remove('bancotemp.txt')
		else:
			valor = float(input("Digite o valor do débito: "))
			if valor > saldo or valor <= 0:
				print ("Saldo insuficiente ou valor de débito inválido.")
				arquivo.close()
				arquivotemp.close()
				os.remove('bancotemp.txt')
			else:
				arquivo = open('banco.txt','w')
				conta = "{0} {1}\n".format(conta,str(saldo - valor))
				arquivotemp.write(conta)
				arquivotemp = open('bancotemp.txt','r')
				copia = arquivotemp.read()
				arquivo.write(copia)
				arquivo.close()
				arquivotemp.close()
				os.remove('bancotemp.txt')
				print ("Débito realizado com sucesso!")
	elif usuario == 5:
		arquivo = open('banco.txt','r')
		arquivotemp = open('bancotemp.txt','a')
		achou_origem = 0
		achou_destino = 0
		conta_origem = input("Digite o numero da conta de origem: ")
		conta_destino = input("Digite o numero da conta de destino: ")
		if conta_destino == conta_origem:
			print ("Não é possível realizar uma transferência para a mesma conta.")
		else:
			for linha in arquivo:
				linhas = linha.split(' ')
				if linhas[0] == conta_origem:
					achou_origem = 1
					saldo_origem = float(linhas[1])
				elif linhas[0] == conta_destino:
					achou_destino = 1
					saldo_destino = float(linhas[1])
				else:
					arquivotemp.write(linha)
			if achou_origem == 0 or achou_destino == 0:
				print ("Uma das contas não foi encontrada. Tente novamente.")
				arquivo.close()
				arquivotemp.close()
				os.remove('bancotemp.txt')
			else:
				valor = float(input("Digite o valor da transferência: "))
				if valor > saldo_origem or valor <= 0:
					print ("Saldo insuficiente ou valor de transferência inválido.")
					arquivo.close()
					arquivotemp.close()
					os.remove('bancotemp.txt')
				else:
					arquivo = open('banco.txt','w')
					contadestino = "{0} {1}\n".format(conta_destino,str(saldo_destino + valor))
					arquivotemp.write(contadestino)
					contaorigem = "{0} {1}\n".format(conta_origem,str(saldo_origem - valor))
					arquivotemp.write(contaorigem)
					arquivotemp = open('bancotemp.txt','r')
					copia = arquivotemp.read()
					arquivo.write(copia)
					arquivo.close()
					arquivotemp.close()
					os.remove('bancotemp.txt')
					print ("Transferência realizada com sucesso!")
	elif usuario == 6:
		arquivo = open('banco.txt','r')
		achou = 0
		conta = input("Para verificar o saldo, digite o numero da conta: ")
		for linha in arquivo:
			linhas = linha.split(' ')
			if linhas[0] == conta:
				achou = 1
				saldo = float(linhas[1])
		if achou == 0:
			print ("Conta não encontrada. Tente novamente.")
			arquivo.close()
		else:
			print ("Saldo da conta: ",saldo)
			arquivo.close()
	else:
		print ("Operação inválida. Tente novamente")
