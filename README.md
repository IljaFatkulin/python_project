# Pasākumu un Kategoriju Pārvaldības Lietotne

## Projekta uzdevums

Šī projekta mērķis ir izveidot konsoles lietotni Python valodā, kas ļauj lietotājam veidot, skatīt, rediģēt un dzēst dažādus **pasākumus** un **kategorijas**. Projekts izmanto MongoDB datubāzi, lai saglabātu datus, un nodrošina vienkāršu saskarni darbībām ar pasākumiem un to kategorijām.

Galvenās funkcionalitātes:
- Jaunu kategoriju pievienošana, skatīšana, dzēšana un rediģēšana
- Jaunu pasākumu pievienošana, skatīšana, dzēšana, rediģēšana
- Pasākumu meklēšana pēc nosaukuma vai datuma
- Pasākumu skatīšana tuvāko 24 stundu laikā
- Pasākumu skatīšana pēc kategorijas

## Izmantotās Python bibliotēkas

Projektā izmantotas šādas bibliotēkas:

### `pymongo`
- **Mērķis:** Savienojuma izveide un mijiedarbība ar MongoDB datubāzi.
- **Kāpēc nepieciešams:** Tā kā dati tiek glabāti MongoDB mākonī, `pymongo` ir nepieciešams, lai veiktu CRUD (Create, Read, Update, Delete) operācijas ar datubāzi.

### `datetime`
- **Mērķis:** Darbs ar datumiem un laikiem (piemēram, pasākumu datumu saglabāšanai, filtrēšanai pēc laika u.c.).
- **Kāpēc nepieciešams:** Lietotājs var ievadīt pasākuma datumu un laiku, un nepieciešams pareizi kombinēt šo informāciju, kā arī salīdzināt un filtrēt pasākumus, pamatojoties uz datuma kritērijiem.

## Pašdefinētas datu struktūras

Projektā ir izmantotas divas galvenās datu struktūras, kas definētas kā Python klases:

### `Category` klase (`category.py`)
- Satur informāciju par kategoriju (`name`, `id`)
- Ietver metodi `save()`, kas saglabā vai atjaunina datus datubāzē.

### `Event` klase (`event.py`)
- Apraksta pasākumu ar šādiem atribūtiem: `name`, `category_id`, `category_name`, `date`, `description`, `id`
- Ietver metodi `save()`, lai ievietotu vai atjauninātu pasākumu datubāzē
- `__str__` metode ļauj ērti izvadīt informāciju par pasākumu

Šīs klases atvieglo datu organizēšanu un loģiku, atdalot to no MongoDB vaicājumiem.

## Programmatūras izmantošanas metodes

Lietotnes galvenā ieejas punkta fails ir `main.py`, kurš nodrošina izvēlni starp kategoriju un pasākumu pārvaldības funkcijām.

### Lietotāja izvēlnes piemērs:

```text
1. Category Actions
2. Event Actions
3. Exit
Choose an option:
