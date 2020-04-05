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

  Given Estoy en la sección de Book a Flight y quiero registrar los datos de los Pasajeros del vuelo
  When Escribo el nombre del primer pasajero "Primer" y el apellido del primer pasajero "Primero" y la preferencia en alimentos es diabetica "DBML", escribo el nombre del segundo pasajero "Segundo", el apellido del segundo pasajero "Segundo" que es Vegetariano "VGML"
  Then El sistema me registra los datos de los pasajeros

  Given Estoy en la sección de Book a Flight y quiero registrar los datos de la tarjeta de crédito
  When Selecciono el tipo de tarjeta de crédito Diners Club "DC" y ingreso el numero de la tarjeta de credito "1234567890123456" y selecciono la fecha de expiracion su mes "10", y el año "2010", ingreso mi nombre "Julian" mi segundo nombre " " y apellido "Gómez"
  Then El sistema me registra los datos de la tarjeta de credito

  Given Estoy en la sección de Book a Flight y quiero registrar los datos de mi dirección de facturación
  When No Quiero que sea ticketless e ingreso mi dirección principal "123 Calle Falsa" no ingreso nada en la direccion secundaria " " de la ciudad "Medellin" cuya provincia es Antioquia "ANT" mi codigo postal es "050001" y mi país es Colombia con código "42" y acepto el excedente de 6.5usd
  Then El sistema me registra los datos de la dirección de facturación

  Given Estoy en la sección de Book a Flight y quiero registrar los datos de mi dirección de envio
  When No Quiero que sea la misma direccion de facturación e ingreso mi dirección principal "321 Calle 20" no ingreso nada en la direccion secundaria " " de la ciudad "Envigado" cuya provincia es Antioquia "ANT" mi codigo postal es "050001" y mi país es Colombia con código "42" y acepto el excedente de 6.5usd
  Then El sistema me registra los datos de la dirección de envio y realiza el booking

  Given Estoy en la pagina de Mercury Tours y quiero terminar la confirmación del vuelo
  When Verifico los datos que se muestran en pantalla, me salgo del sistema
  Then El sistema deberia guardar los datos de la reserva