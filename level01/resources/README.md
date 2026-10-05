# level01

Dans les anciens systèmes Linux, les hashs des mots de passe étaient stockés dans /etc/passwd.

```jsx
cat /etc/passwd | grep flag01
```

On obtient : 42hDRfypTqqnw

Sur le terminal d’une VM KaliLinux:

```jsx
echo "42hDRfypTqqnw" > hash.txt
john hash.txt
```

- echo "42hDRfypTqqnw" > hash.txt : met le mot de passe haché dans un fichier texte
- john hash.txt :
    - lit le fichier texte et identifie le type de chiffrement
    - chiffre un par un les mots de passe de sa base de données avec le même type de chiffrement que mon mot de passe haché, et compare le résultat avec le mot de passe haché du fichier pour voir si ca correspond
    - affiche le mot de passe déchiffré sur le terminal et l’enregistre dans un fichier john.pot dans le dossier .john

John affiche le mot de passe en clair : abcdefg
