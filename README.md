# Lyra OS Icons

Tema de ícones oficial do Lyra OS, distribuído separadamente como
`lyra-os-icons`.

## Build

```bash
./scripts/build-icons.sh
rpmbuild -bb packaging/lyra-os-icons.spec
```

O build gera `dist/Lyra-OS-Icons`, com herança de Adwaita para cobertura dos
ícones não personalizados.

## Cor de destaque do GNOME

O build também gera nove variantes `Lyra-OS-Icons-<cor>`: blue, teal, green,
yellow, orange, red, pink, purple e slate, com a paleta nativa do GNOME.
Os links e a herança dos ícones são preservados. A variante base permanece
inalterada para consumidores que usam um tema fixo.

As pastas especiais também acompanham a cor de destaque: Área de Trabalho
(`user-desktop` e `folder-desktop`), Documentos, Downloads, Música, Imagens,
Público, Modelos e Vídeos. A Área de Trabalho usa a pasta Lyra com um símbolo
de monitor, sem depender da cor do ícone herdado do Adwaita.

O pacote `lyra-os-theme` sincroniza a variante com a cor escolhida no GNOME.
Essa integração não escreve configurações de KDE ou XFCE.
