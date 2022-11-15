# Gragas damage optimizer

This program finds the best build to maximize Gragas damages in League of Legends. It prompts the user for multiple parameters to customize the output as much as possible. It was done with Python 3.11 and on LoL patch `12.21`. It will only search in mythic and legendary AP items from this patch, to save on computing time. 

## Usage

```bash
python main.py
```

## Output examples

```bash
> Enemy : 4000 HP - 170 Magic Resist
> Runes : 30 AP - 10 Haste - 5 Magic Pen
> Level : 18 - Q : uncharged
> Golds : ∞ - With Sorcerer's Shoes : True
> Build : 1 Mythic with 4 legendary items
> Maxing : QEW

 === BURST

 3 bests builds :
  1. 2708 dmg : Hextech Rocketbelt - Horizon Focus - Rabadon's Deathcap - Lich Bane - Void Staff
  2. 2684 dmg : Hextech Rocketbelt - Rabadon's Deathcap - Lich Bane - Shadowflame - Void Staff
  3. 2667 dmg : Hextech Rocketbelt - Horizon Focus - Rabadon's Deathcap - Demonic Embrace - Void Staff


 === DPS

 3 bests builds :
  1. 666 dmg/s : Liandry's Anguish - Horizon Focus - Rabadon's Deathcap - Lich Bane - Void Staff
  2. 646 dmg/s : Liandry's Anguish - Cosmic Drive - Rabadon's Deathcap - Lich Bane - Void Staff
  3. 635 dmg/s : Liandry's Anguish - Nashor's Tooth - Rabadon's Deathcap - Lich Bane - Void Staff
```

```bash
> Enemy : 2500 HP - 45 Magic Resist
> Runes : 30 AP - 10 Haste - 5 Magic Pen
> Level : 16 - Q : uncharged
> Golds : ∞ - With Sorcerer's Shoes : True
> Build : 1 Mythic with 2 legendary items
> Maxing : QEW

 === BURST

 3 bests builds :
  1. 2717 dmg : Hextech Rocketbelt - Horizon Focus - Rabadon's Deathcap
  2. 2713 dmg : Hextech Rocketbelt - Lich Bane - Rabadon's Deathcap
  3. 2680 dmg : Hextech Rocketbelt - Shadowflame - Rabadon's Deathcap


 === DPS

 3 bests builds :
  1. 546 dmg/s : Luden's Tempest - Lich Bane - Rabadon's Deathcap
  2. 535 dmg/s : Hextech Rocketbelt - Lich Bane - Rabadon's Deathcap
  3. 532 dmg/s : Liandry's Anguish - Lich Bane - Rabadon's Deathcap
```
