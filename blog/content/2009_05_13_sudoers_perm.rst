sudoers file with restricted permissions
########################################
:date: 2009-05-13 18:10
:author: Ivan Marin
:category: debian
:tags: config, debian, sudo
:slug: 2009_05_13_sudoers_perm
:status: published

O acesso ao sudo é uma ferramenta bem poderosa no linux, mas que
geralmente é mal usada, permitindo que qualquer comando possa ser feito
com sudo, o que é um risco de segurança. O ideal é que os usuários
tenham acesso root a nada, ou a somente os comandos *realmente*
necessários. Aqui no LHC temos um novo aluno que está montando a
plataforma web dos dados de campo. Ele vai precisar acesso ao apache2 e
ao mysql. Para isso, o /etc/sudoers foi configurado da seguinte forma:#
/etc/sudoers

::

    #
    # This file MUST be edited with the 'visudo' command as root.
    #
    # See the man page for details on how to write a sudoers file.
    #

    Defaults    env_reset

    # Host alias specification

    # User alias specification

    # Cmnd alias specification
    Cmnd_Alias APACHE_START = /etc/init.d/apache2 start
    Cmnd_Alias APACHE_STOP = /etc/init.d/apache2 stop
    Cmnd_Alias APACHE_RESTART = /etc/init.d/apache2 restart
    Cmnd_Alias MYSQL = /usr/bin/mysql
    # User privilege specification
    root    ALL=(ALL) ALL
    ispmarin ALL=(ALL) NOPASSWD:ALL
    pucciarelli ALL=APACHE_START, APACHE_STOP,APACHE_RESTART,MYSQL
    # Uncomment to allow members of group sudo to not need a password
    # (Note that later entries override this, so you might need to move
    # it further down)
    # %sudo ALL=NOPASSWD: ALL

O que permite que o usuário só acesse esses comandos,  o que é
excelente.

Edit 23/05: está funcionando a contento. O usuário está conseguindo
trabalhar corretamente com o Drupal na isengard sem precisar de mais
acesso ao sistema, o que é ótimo, pois a isengard é a minha máquina de
trabalho diário e meu servidor de arquivos.
