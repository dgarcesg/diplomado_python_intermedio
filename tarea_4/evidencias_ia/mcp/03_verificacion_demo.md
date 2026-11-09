# Verificación independiente de la demostración del MCP

Las cifras que dio Claude Code con el MCP `bcrp` (ver `01_demo_mcp_claude_code.txt` y `02_demo_mcp_claude_code_completa.md`)
se recalcularon pidiendo los datos **directamente a las APIs**, sin pasar por `mcp/server.py`:

    python evidencias_ia/mcp/verificar_demo.py

Ejecutado el 8 de noviembre de 2026.

| Afirmación de la demo | Valor en la demo | Valor recalculado | Fuente | ¿Coincide? |
|---|---:|---:|---|:---:|
| Inflación 12 meses Lima, ene-2020 | 1.89 % | 1.888 % | BCRP API, PN01273PM | ✅ |
| Inflación 12 meses Lima, dic-2024 | 1.97 % | 1.966 % | BCRP API, PN01273PM | ✅ |
| Máximo 2020-2024 | 8.81 % (2022-06) | 8.813 % (Jun.2022) | BCRP API, PN01273PM | ✅ |
| Mínimo 2020-2024 | 1.60 % (2020-06) | 1.599 % (Jun.2020) | BCRP API, PN01273PM | ✅ |
| Promedio 2020-2024 (60 meses) | 4.47 % | 4.466 % | BCRP API, PN01273PM | ✅ |
| Cobre Cajamarca, mes máximo 2024 | 2,349.4 tm.f (2024-11) | 2,349.36 (Nov.2024) | BCRP API, RD12956DM | ✅ |
| Cobre Cajamarca, promedio mensual 2024 | 1,932.9 tm.f | 1,932.93 | BCRP API, RD12956DM | ✅ |
| Crecimiento promedio del PBI 2015-2024, Perú | 2.44 % | 2.44 % | Banco Mundial, NY.GDP.MKTP.KD.ZG | ✅ |
| Ídem, Chile | 2.06 % | 2.06 % | Banco Mundial | ✅ |
| Ídem, Colombia | 2.54 % | 2.54 % | Banco Mundial | ✅ |

Las diferencias son solo de redondeo: el MCP redondea a 2 decimales para presentar.

## Problemas encontrados en la demo

- **El prompt `/mcp__bcrp__informe` recibe solo la primera palabra del tema.** Con `tipo de cambio` llegó `tipo`.
  Claude Code separa los argumentos por espacios y el prompt tiene un solo argumento. El agente lo detectó y lo
  corrigió solo. Para temas de varias palabras hay que usar comillas (`/mcp__bcrp__informe "tipo de cambio"`).
- **`variacion_pct` no tiene sentido en series que ya son porcentajes**, como la inflación: en ese caso lo que
  sirve es `cambio`, en puntos porcentuales. La descripción de `resumen` lo advierte y el agente lo aplicó bien.
- **La fecha de fin del catálogo del BCRP va atrasada**, por ejemplo dic-2025, cuando la API ya tiene datos hasta
  sep-2026. Por eso el recurso la muestra como `fin_segun_catalogo`.
- **La primera orden de la demo fue `/mcp.bcrp`**, que no es un comando. Claude Code la interpretó como un pedido de
  probar el servidor y lo hizo, con una llamada a cada herramienta, al recurso y a las pruebas.
