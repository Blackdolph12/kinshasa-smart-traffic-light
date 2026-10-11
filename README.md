# 🚦 Kinshasa Smart Traffic Light
### Feu de Circulation Solaire Intelligent - Grande Voie Kinshasa 🇨🇩

> 100% solaire | Contrôlé par téléphone 4G | Open Source | Made in Congo

## 🎯 Le Problème / The Problem
Les grandes routes de Kinshasa (Blvd 30 Juin, Triomphal, Matadi) n'ont pas assez de feux. Embouteillages, accidents. Pas de courant SNEL.

Big roads in Kinshasa have no traffic lights. No power. This project solves it with solar.

## 💡 La Solution
Feu tricolore 300mm:
- 2x Panneaux solaires 100W
- Batterie LiFePO4 12V 100Ah = 72h sans soleil
- Contrôleur Raspberry Pi 4 + 4G Airtel/Vodacom
- Contrôle depuis téléphone partout à Kinshasa

### Modes:
1. AUTO: Vert 90s / Jaune 5s / Rouge 120s (pour grande voie)
2. MANUAL: Contrôle par Telegram bot
3. POLICE: Vert bloqué pour passage VIP
4. PANNE: Jaune clignotant

## 🛒 Liste d'Achats Kinshasa (1 carrefour)
Voir dossier `/hardware` - Total: ~$370 (petit) à $900 (grande voie 6m)

- Marché Gambela (Gombe): moins cher
- Zando (Limete): LED traffic heads
- Jumia RDC: livraison

## 💻 Code
```python
# Voir /firmware/traffic_controller.py
# Contrôle automatique pour grande voie