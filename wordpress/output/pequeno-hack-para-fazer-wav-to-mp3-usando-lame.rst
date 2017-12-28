Pequeno hack para fazer wav to mp3 usando lame
##############################################
:date: 2009-10-05 20:39
:author: ispmarin
:category: debian
:slug: pequeno-hack-para-fazer-wav-to-mp3-usando-lame
:status: published

Simples assim:

for i in \*.wav ; do lame --vbr-new -B 320 -q 2 ^Ci" "\`basename "$i"
.wav\`".mp3; done

onde o for é para pegar todos os arquivos do diretório, --vbr-new é para
converter usando variable bitrate, -B é para converter em 320Kbps, e é
tudo o que precisa.

for file in \*.flac; do $(flac -cd "$file" \| lame -h -
"${file%.flac}.mp3"); done
