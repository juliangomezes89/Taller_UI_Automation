Feature: Reservar un vuelo en Mercury Tours
 Scenario:
  Given Estoy en la pagina de Mercury Tours y quiero loguearme para reservar un vuelo
  When Ingreso un usuario "jgomeze4" y un password "Manchas.1232" para acceder
  Then El sistema me autentica como usuario legitimo y continuo a reservar

  Given Estoy en la sección de Flight Finder y requiero buscar un vuelo
  When Selecciono el tipo de vuelo "roundtrip" y  requiero tiquetes para "2" pasajeros, saliendo desde "Zurich" en el mes "5" del día "25" y con destino a "Paris" regresando el mes "6" del dia "1", en clase "Business" sin ninguna areolina de preferencia
  Then El sistema realiza la busqueda de los vuelos diponibles con estos parametros de búsqueda

  Given Estoy en la sección de select Flight y quiero seleccionar un vuelo
  When Selecciono el vuelo de origen con la aerolinea "Unified" y el vuelo de regreso con la aerolinea "Unified"
  Then El sistema me confirma la seleccion de los vuelos para reservarlos a continuación