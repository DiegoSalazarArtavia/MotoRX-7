"""Excepciones propias del sistema."""


class MotoRXError(Exception):
    """Excepción base de todo el sistema."""


class ValidacionError(MotoRXError):
    """Un dato no cumple una validación. Indica el campo y el motivo."""

    def __init__(self, campo: str, motivo: str) -> None:
        self.campo = campo
        self.motivo = motivo
        super().__init__(f"{campo}: {motivo}")


class IdDuplicadoError(ValidacionError):
    """Se intentó registrar un identificador que ya existe."""

    def __init__(self, identificador: str) -> None:
        super().__init__("id", f"ID duplicado ({identificador})")
        self.identificador = identificador


class ReferenciaInexistenteError(ValidacionError):
    """Se hace referencia a un recurso o actividad que no existe."""


class CicloDependenciaError(ValidacionError):
    """Las dependencias forman un ciclo. Guarda la cadena afectada."""

    def __init__(self, cadena: list[str]) -> None:
        super().__init__("dependencias", "ciclo detectado: " + " -> ".join(cadena))
        self.cadena = cadena


class OperacionNoPermitidaError(MotoRXError):
    """La operación no se puede realizar en el estado actual."""


class EscenarioInvalidoError(MotoRXError):
    """Un escenario cargado o generado tiene errores de esquema o referencias."""

    def __init__(self, errores: list[str]) -> None:
        super().__init__("; ".join(errores))
        self.errores = errores


class PersistenciaError(MotoRXError):
    """Error al guardar o recuperar información (por ejemplo, archivo corrupto)."""
