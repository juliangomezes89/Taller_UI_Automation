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
