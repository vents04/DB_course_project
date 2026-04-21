# Стратегия за сигурност и роли
- **Вход:** Firebase Auth (Email/Password). В демото КЕП е заменено с парола — в реалната система автентикацията е биометрия/ПИН в Bulbank Mobile.
- **Автоматично разпознаване на роли при регистрация:**
  - `@supervisor.ucb.bg` → `role: supervisor`
  - `@ucb.bg` (без `supervisor.`) → `role: specialist`
  - всичко останало → `role: customer`
- **Защита на пътищата:**
  - `PrivateRoute role="specialist"` пази `/specialist/*`.
  - `PrivateRoute role="supervisor"` пази `/supervisor/*`.
  - Клиентът няма достъп до вътрешни пътища; ако опита, се пренасочва към `/my-complaints`.
