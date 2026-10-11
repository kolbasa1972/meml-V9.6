#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MEML 9.6 — ЧЁРНЫЕ ДЫРЫ (минимальный расчёт)
Только физика ЧД. Без теории, без V9.6.
"""

# Входные параметры (масса аксиона)
m_a_eV = 5.63e-6           # эВ

# Константы СИ
eV_to_J = 1.602176634e-19
c       = 2.99792458e8     # м/с
G       = 6.67430e-11      # м³/(кг·с²)
hbar    = 1.054571817e-34  # Дж·с
M_sun   = 1.98892e30       # кг
M_Pl    = 1.22e19          # ГэВ

# Перевод массы в кг
m_a_kg = m_a_eV * eV_to_J / c**2

print("=" * 60)
print("  ЧЁРНЫЕ ДЫРЫ И АКСИОН (m_a = 5.63 мкэВ)")
print("=" * 60)
print()

# 1. Критическая масса ЧД (суперадиантность)
# M_BH = 0.5 · ℏc / (G · m_a)
M_BH_kg = 0.5 * hbar * c / (G * m_a_kg)
M_BH_solar = M_BH_kg / M_sun

print(f"1. Критическая масса ЧД:")
print(f"   M_BH = {M_BH_solar:.3e} M_⊙")
print()

# 2. Критическая масса аксионной звезды
# M_crit ~ M_Pl² / m_a
m_a_GeV = m_a_eV * 1e-9
M_crit_GeV = M_Pl**2 / m_a_GeV
M_crit_kg = M_crit_GeV * eV_to_J * 1e9 / c**2
M_crit_solar = M_crit_kg / M_sun

print(f"2. Критическая масса аксионной звезды:")
print(f"   M_crit = {M_crit_solar:.3e} M_⊙")
print()

# 3. Условие суперадиантности
# ω_a < Ω_H
omega_a = m_a_eV * eV_to_J / hbar           # рад/с
Omega_H = c**3 / (2 * G * M_BH_kg)          # рад/с

print(f"3. Условие суперадиантности:")
print(f"   ω_a   = {omega_a:.3e} рад/с")
print(f"   Ω_H   = {Omega_H:.3e} рад/с")
print(f"   ω_a < Ω_H: {omega_a < Omega_H}")
print()

# 4. Совпадение масс
print(f"4. Отношение масс:")
print(f"   M_BH / M_crit = {M_BH_solar / M_crit_solar:.4f}")
print()

print("=" * 60)