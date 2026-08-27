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
