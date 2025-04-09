import matplotlib.pyplot as plt
import seaborn as sns
from math import pi
import pandas as pd

# --- Données ---
data = {
    'commandes': 500,
    'commandes_livrees_a_temps': 420,
    'stock_moyen': 120000,
    'ventes_net': 600000,
    'cout_biens_vendus': 450000,
    'taux_possession': 0.25,
    'commandes_parfaites': 385,
    'cout_total_transport': 75000,
    'tonnage_total': 1500,
    'delais_livraisons_fournisseurs': [True, True, False, True, False, True, True, True, False, True],
}

# --- KPI ---
ponctualite_client = data['commandes_livrees_a_temps'] / data['commandes'] * 100
ISR = data['stock_moyen'] / data['ventes_net']
cout_possession_stock = data['stock_moyen'] * data['taux_possession']
ponctualite_fournisseur = sum(data['delais_livraisons_fournisseurs']) / len(data['delais_livraisons_fournisseurs']) * 100
DSI = (data['stock_moyen'] / data['cout_biens_vendus']) * 365
cout_transport_par_tonne = data['cout_total_transport'] / data['tonnage_total']
perfect_order_rate = data['commandes_parfaites'] / data['commandes'] * 100

# --- Résultats KPI ---
kpis = {
    "Ponctualité Client (%)": round(ponctualite_client, 2),
    "ISR (Stock / Ventes)": round(ISR, 2),
    "Coût possession stock (€)": round(cout_possession_stock, 2),
    "Ponctualité Fournisseur (%)": round(ponctualite_fournisseur, 2),
    "DSI (jours)": round(DSI, 1),
    "Coût transport / tonne (€)": round(cout_transport_par_tonne, 2),
    "Commandes Parfaites (%)": round(perfect_order_rate, 2)
}

# --- Barplot des KPI ---
plt.figure(figsize=(12, 6))
sns.barplot(x=list(kpis.keys()), y=list(kpis.values()), palette="viridis")
plt.title("KPI Logistiques - Vue Globale")
plt.ylabel("Valeur")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# --- Radar Chart (KPI normalisés) ---
# Normalisation
max_values = {
    "Ponctualité Client (%)": 100,
    "ISR (Stock / Ventes)": 1.0,
    "Coût possession stock (€)": 50000,
    "Ponctualité Fournisseur (%)": 100,
    "DSI (jours)": 180,
    "Coût transport / tonne (€)": 100,
    "Commandes Parfaites (%)": 100
}
normalized_kpis = {k: min(v / max_values[k], 1.0) for k, v in kpis.items()}

# Préparer pour le radar chart
labels = list(normalized_kpis.keys())
stats = list(normalized_kpis.values())

# Fermer la boucle pour le radar
stats += stats[:1]
angles = [n / float(len(labels)) * 2 * pi for n in range(len(labels))]
angles += angles[:1]

# Tracer le radar
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.plot(angles, stats, linewidth=2, linestyle='solid')
ax.fill(angles, stats, 'skyblue', alpha=0.4)
ax.set_yticklabels([])

# Correction ici : bien mettre les ticks
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=10)
plt.title("Radar des KPI logistiques (normalisé)", size=14)
plt.tight_layout()
plt.show()
