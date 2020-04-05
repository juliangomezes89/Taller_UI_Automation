from behave import *

from ui_testing.tests.booking import BookingTest

booking = BookingTest()

@given(u'Estoy en la pagina de Mercury Tours y quiero loguearme para reservar un vuelo')
def step_impl(context):
    booking.setUpClass()
    booking.test_go_url('http://newtours.demoaut.com/')


@when(u'Ingreso un usuario "{user}" y un password "{password}" para acceder')
def step_impl(context, user, password):
    context.user = user
    context.password = password
    booking.test_login(context.user, context.password)


@then(u'El sistema me autentica como usuario legitimo y continuo a reservar')
def step_impl(context):
    booking.test_image()
    #booking.tearDownClass()

@given(u'Estoy en la sección de Flight Finder y requiero buscar un vuelo')
def step_impl(context):
    pass


@when(u'Selecciono el tipo de vuelo "{tripType}" y  requiero tiquetes para "{passCount}" pasajeros, saliendo desde "{fromPort}" en el mes "{fromMonth}" del día "{fromDay}" y con destino a "{toPort}" regresando el mes "{toMonth}" del dia "{toDay}", en clase "{servClass}" sin ninguna areolina de preferencia')
def step_impl(context, tripType, passCount, fromPort, fromMonth, fromDay, toPort, toMonth, toDay, servClass):
    booking.test_filters(tripType, passCount, fromPort, fromMonth, fromDay, toPort, toMonth, toDay, servClass)


@then(u'El sistema realiza la busqueda de los vuelos diponibles con estos parametros de búsqueda')
def step_impl(context):
    pass

@given(u'Estoy en la sección de select Flight y quiero seleccionar un vuelo')
def step_impl(context):
    pass


@when(u'Selecciono el vuelo de origen con la aerolinea "{outFlight}" y el vuelo de regreso con la aerolinea "{inFlight}"')
def step_impl(context, outFlight, inFlight):
    booking.test_select_flight(outFlight, inFlight)



@then(u'El sistema me confirma la seleccion de los vuelos para reservarlos a continuación')
def step_impl(context):
    pass

@given(u'Estoy en la sección de Book a Flight y quiero registrar los datos de los Pasajeros del vuelo')
def step_impl(context):
    pass


@when(u'Escribo el nombre del primer pasajero "{passFirst1}" y el apellido del primer pasajero "{passLast1}" y la preferencia en alimentos es diabetica "{pass1meal}", escribo el nombre del segundo pasajero "{passFirst2}", el apellido del segundo pasajero "{passLast2}" que es Vegetariano "{pass2meal}"')
def step_impl(context, passFirst1, passLast1, pass1meal, passFirst2, passLast2, pass2meal,):
    booking.test_book_flight_select_2pass(passFirst1, passLast1, pass1meal, passFirst2, passLast2, pass2meal)


@then(u'El sistema me registra los datos de los pasajeros')
def step_impl(context):
    pass

@given(u'Estoy en la sección de Book a Flight y quiero registrar los datos de la tarjeta de crédito')
def step_impl(context):
    pass


@when(u'Selecciono el tipo de tarjeta de crédito Diners Club "{creditCard}" y ingreso el numero de la tarjeta de credito "{creditnumber}" y selecciono la fecha de expiracion su mes "{cc_exp_dt_mn}", y el año "{cc_exp_dt_yr}", ingreso mi nombre "{cc_first_name}" mi segundo nombre "{cc_mid_name}" y apellido "{cc_last_name}"')
def step_impl(context, creditCard, creditnumber, cc_exp_dt_mn, cc_exp_dt_yr, cc_first_name, cc_mid_name, cc_last_name):
    booking.test_credit_card(creditCard, creditnumber, cc_exp_dt_mn, cc_exp_dt_yr, cc_first_name, cc_mid_name, cc_last_name)

@then(u'El sistema me registra los datos de la tarjeta de credito')
def step_impl(context):
    pass

@given(u'Estoy en la sección de Book a Flight y quiero registrar los datos de mi dirección de facturación')
def step_impl(context):
    pass


@when(u'No Quiero que sea ticketless e ingreso mi dirección principal "{billAddress1}" no ingreso nada en la direccion secundaria "{billAddress2}" de la ciudad "{billCity}" cuya provincia es Antioquia "{billState}" mi codigo postal es "{billZip}" y mi país es Colombia con código "{billCountry}" y acepto el excedente de 6.5usd')
def step_impl(context, billAddress1, billAddress2, billCity, billState, billZip, billCountry):
    booking.test_billing_address(billAddress1, billAddress2, billCity, billState, billZip, billCountry)


@then(u'El sistema me registra los datos de la dirección de facturación')
def step_impl(context):
    pass

@given(u'Estoy en la sección de Book a Flight y quiero registrar los datos de mi dirección de envio')
def step_impl(context):
    pass


@when(u'No Quiero que sea la misma direccion de facturación e ingreso mi dirección principal "{delAddress1}" no ingreso nada en la direccion secundaria "{delAddress2}" de la ciudad "{delCity}" cuya provincia es Antioquia "{delState}" mi codigo postal es "{delZip}" y mi país es Colombia con código "{delCountry}" y acepto el excedente de 6.5usd')
def step_impl(context, delAddress1, delAddress2, delCity, delState, delZip, delCountry ):
    booking.test_delivery_address(delAddress1, delAddress2, delCity, delState, delZip, delCountry)

@then(u'El sistema me registra los datos de la dirección de envio y realiza el booking')
def step_impl(context):
    booking.test_buyFlights()

@given(u'Estoy en la pagina de Mercury Tours y quiero terminar la confirmación del vuelo')
def step_impl(context):
    pass


@when(u'Verifico los datos que se muestran en pantalla, me salgo del sistema')
def step_impl(context):
    booking.test_logout()


@then(u'El sistema deberia guardar los datos de la reserva')
def step_impl(context):
    booking.tearDownClass()

