l# 🚦 Kinshasa Smart Traffic Light
### Feu de Circulation Solaire Intelligent - Grande Voie Kinshasa

![Kingabwa](https://raw.githubusercontent.com/blackdolph12/kinshasa-smart-traffic-light/main/render-kingabwa.jpg)

> 100% solaire | Contrôlé par téléphone 4G | Open Source | Made in Congo 🇨🇩

### 📍 Site Pilote #1: Kingabwa - Limete - Kinshasa
Feu solaire installé à Kingabwa, route poussiéreuse avec camions, taxis jaunes, marché. **Pas de SNEL? Pas de problème!** Notre système fonctionne 72h sans soleil.

**Prochain site:** Gombe - Boulevard du 30 Juin (grande voie 6m)

## 🎯 Le Problème / The Problem
Les grandes routes de Kinshasa (Blvd 30 Juin, Triomphal, Matadi) n'ont pas de feux ou feux cassés. Résultat: embouteillages monstres, accidents, pas de régulation.

Big roads in Kinshasa have no traffic lights. No SNEL power, no control. Chaos!

## 💡 La Solution
**Feu tricolore 300mm pour grande voie:**
- 2x Panneaux solaires 100W = 200W total
- Batterie LiFePO4 12V 100Ah = **72h sans soleil**
- Contrôleur Raspberry Pi 4 + 4G Airtel/Vodacom/Orange
- Contrôle depuis téléphone partout à Kinshasa via Telegram
- Boîtier IP65 + poteau 6 mètres
- Coût: $370 (DIY) à $900 (version pro) - vs $27,500 ancien robot!

### Modes:
1. **AUTO:** Vert 90s / Jaune 5s / Rouge 120s (pour grande voie)
2. **MANUAL:** Contrôle via Telegram bot depuis téléphone
3. **POLICE:** Vert bloqué pour VIP / convoi officiel
4. **PANNE:** Jaune clignotant si problème

## 🛒 Liste d'Achats - Où acheter à Kinshasa
- Marché Gambela / Zando
- Limete - 7ème rue - magasins électroniques
- Jumia RDC - Panneaux solaires
- Prix total: $370 - $900 selon qualité

## 💻 Code
Le code complet est dans `firmware/traffic_controller.py`
- Python - Open Source
- Fonctionne avec Raspberry Pi
- Contrôle 4G via Telegram

## 🚀 Comment contribuer
1. Fork ce repo
2. Ajoute ton amélioration
3. Pull request

Made with ❤️ in Kinshasa - Pour résoudre le trafic de Kinshasa!

**Contact:** Projet par blackdolph12

#Kinshasa #SmartCity #Solar #RDC #TrafficLight #OpenSource