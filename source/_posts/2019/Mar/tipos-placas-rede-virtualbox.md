---
title: Tipos de placas de rede no VirtualBox
date: 2019-03-12 19:00
tags: [virtualbox, rede, virtualizacao]
category: VMs
linkTitle: tipos-de-placas-de-rede-no-virtualbox
summary: Conheça todos os tipos de placa de rede no virtalbox e entada para que 
         e como usar.
---


O VirtualBox já é um velho conhecido dos usuários de linux <s>que ficam testando
todas as distros do distrowatch</s> aficionados por conhecer novos sitemas
operacionais. Mas como nem só de testes de SOs vive a virtualização, o VBOX 
traz muitas possibilidades para o estudo de redes.

Sabe quando o seu professor de Sistemas Distribuidos passa aquele trabalho de
configurar dois servidores: um com Windows Server e outro com CentOS trabalhando
juntos e você <s>chora so de pensar em ter que instalar o Windows de novo, ou 
aquele Gnome Horroso do CentOS</s> não quer fazer dualboot com aquele seu
manjaro recem instalado? Pra isso existe a **Placa em modo Bridge** que permite 
ao seu sistema convidado ter acesso a rede local do hospedeiro, em outras
palavras: A nossa máquina virtual será vista como uma máquina física na rede
local, com ip diferente da máquina hospedeira e tudo! Dessa forma você pode
conectar dois Notebooks em um mesmo roteador, instala o Windows Server em um
e o CentOS em outro e configura ambas VMs para funcionarem em modo Bridge e
sem ter que instalar os sitemas fisicamente.

O **Modo NAT** não traz muitas novidades pra quem ja está testando distros
ele é o padrão do virtualbox e basicamente conecta a maquina virtual a internet
tendo a máquina hospedeira como gateway.

Agora se você não quer interferir na rede local, pra não acabar derrubando a
internet da sua casa, existe o modo de **Rede Interna** que permite criar uma
rede apenas entre as VMs, o que é perfeito para simular Sistemas que rodem
dentro de uma Intranet.

Já a Rede em modo **host only** O VirtualBox monta uma rede apenas com o
hospedeiro e as VMs, e um híbrido entre o modo Bridge, pois as VMs enxergam o
hospedeiro, e o modo de Rede Interna, pois as VMs se enxergão entre si.

P. S.: Ja estava com um rascunho desse post quando estava estudando sobre redes,
e como agora tenho que instalar um servidor com CentOS que converse com o
Windows Server consegui terminar de escrever!


