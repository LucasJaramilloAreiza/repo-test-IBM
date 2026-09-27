# repo-test-IBM

Este es un repositorio de prueba diseñado específicamente para validar una herramienta de **Code Review Automatizada** basada en 4 agentes especializados:

1. **Security Sentinel**: Encargado de detectar vulnerabilidades de seguridad.
2. **Logic Auditor / Acceptance Criteria**: Encargado de validar que el código cumple con los requerimientos de negocio y no introduce bugs lógicos.
3. **Performance Hawk**: Encargado de detectar cuellos de botella y antipatrones de rendimiento.
4. **Blast-Radius Mapper**: Encargado de identificar el impacto colateral (breaking changes) de modificaciones en componentes compartidos.

## Estructura
El proyecto es una mini API de e-commerce construida con **FastAPI** y **SQLite**.

- La rama `main` contiene el código base funcional.
- La rama `feature/checkout-update` contiene un intento de implementación de un nuevo endpoint de pagos (`/checkout`) que deliberadamente introduce 4 defectos clave, uno para cada agente validador.

## Instrucciones para la Prueba
Para ejecutar la prueba del sistema de Code Review, se debe abrir un **Pull Request** desde la rama `feature/checkout-update` hacia la rama `main`. El archivo `PR_DESCRIPTION.md` contiene el texto sugerido para la descripción del PR.
