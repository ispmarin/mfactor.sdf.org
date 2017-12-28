Diferenças entre Ubuntu e Debian
################################
:date: 2009-07-09 12:05
:author: ispmarin
:category: debian
:tags: debian, development, open source, ubuntu
:slug: diferencas-entre-ubuntu-e-debian
:status: published

Lendo a lista de usuários Debian (debian-user), vi uma discussão que
achei muito interessante, sobre as principais diferenças entre o Debian
e o Ubuntu. O autor, AndyC, liberou o artigo para ser postado no
wiki.debian.org, então reproduzo aqui o post. Leitura muito
interessante, que vou tentar depois traduzir para o Português.

+++++++++++++++++++++++++++++

Post deAndrew Carter, debian-user@

| Lots of differences: some big, some small but all may be significant.
  I
|  am \_NOT\_speaking in an official capacity for the Debian project or,
|  indeed, for Ubuntu to whom I'm also a contributor.

| When Ubuntu first started, one of their developers said to me "If we
|  could have called it Debian for desktops, we would have done". That
  was
|  their focus then: it has widened significantly now. But the core
  focus
|  for Ubuntu remains the user experience and a small core of
  applications.

Largely subjectively, from as far to the outside as I can get :)

| Rationale/design goals
|  ======================

| Packages in Ubuntu main are very highly polished, very well maintained
|  and Canonical/Ubuntu go the extra mile to make the experience easy
  for
|  the user. That comes at one or more of several costs:

| Choice
|  ======

| Lack of choice - you get one mail client rather than a choice of
|  several "out of the box", for example. Choices are made for you - its
  an
|  issue of supportability. Debian offers you more flexibility at the
  price
|  of complexity or being willing to support your choices.

| Architectures
|  =============

| Lack of architectures: if you're not on Intel/AMD64 or, possibly,
|  ARM/Sparc/PPC (depending on release) - you can't run Ubuntu. Debian
|  running on 11 or so architectures does mean that a) the process is
|  sometimes slow b) the code gets debugged c) is made portable/fixes
  are
|  contributed upstream.

| Developer/user ratio
|  ====================

| Canonical has relatively few paid developers, a highly motivated
|  volunteeer developer community, a much larger community advocacy and
|  marketing budget and a vast number of new users. This does
|  mean that their developers are massively outnumbered by their users
  and
|  priorities have to be set. Packages in universe/multiverse may
  therefore
|  receive less attention than those in main in Ubuntu.

| At least in theory, every package in Debian is equal and has a known
  named
|  maintainer who takes an interest :) It does mean that Debian does
  much of
|  the heavy lifting of packaging and initial support for out of the way
|  packages - it also means that, if I want support for R and CRAN, for
  example,
|  I'd go straight to Debian because the maintainer has a personal and
|  professional interest for seeing it work well as an integrated
  system.

| Release cycles
|  ==============

| "We demand rigidly defined areas of doubt and uncertainty" - Canonical
|  has those because it releases once every six months. This consistency
|  comes at a price: users expect new whizzy features with each release
  and
|  the development cycle is very short indeed. Long term support
  releases
|  happen every 18 months and are supported for three years on the
|  desktop/five years on the server. That's hard. It's \_very\_ hard to
|  support new hardware with long term releases. "Normal" releases may
  mix
|  packages from Debian stable with testing, unstable or even
  experimental
|  (whizzy features) but get only a short testing time.

| Debian "releases when ready" but then supports that release until
  about
|  a year after the \_next\_ release. 22 months to release Etch, 22
  months to
|  release Lenny + 12 months = 56 months. Slow moving progress through
|  testing to release, regular point updates with security fixes.

| Freeness vs. pragmatism
|  =======================

| Ubuntu may sometimes take a pragmatic attitude for "software that
  works"
|  for users. They also have the ability, which Debian does not, to
  enter
|  into commercial agreements for third party apps e.g. Oracle/VMWare.
|  [DFSG - not "licence just for Debian"]. Canonical benefits from
  Debian
|  idealism but it can't flow the other way :(

| Upgrades between releases
|  =========================

| You'll hear lots of views on this. SUBJECTIVE OPINION FOLLOWS:GUT
|  FEELING AND EXPERIENCE IN EQUAL PARTS. Ubuntu is harder to upgrade
|  cleanly between releases and it may actually be quicker to reinstall.
|  You certainly can't skip a release so you'd need to do 8.04, 8.10,
|  9.04, 9.10 (for example). This is partly a consequence of short
  release
|  cycles above. Debian is \_far\_ more polished here /SUBJECTIVE

| Summary
|  =======

| All of this is very well explained by The Official Ubuntu Book and
  Mark
|  Shuttleworth's latest interview for ?? Linux Format ?? magazine.
|  Its also worth reading newsgroups/fora and planet.debian.org /
|  planet.ubuntu.com to get a better appreciation of the similarities
  and
|  differences in approach. Debian and Ubuntu each have strengths: its a
|  (sometimes uneasy) symbiosis - both distributions share many of the
  same
|  developers, for example, but not necessarily end goals - but Debian
|  gains as much as Ubuntu if they'll just fix their bloody bug #1 :)

Hope this helps,

AndyC

+++++++++++
