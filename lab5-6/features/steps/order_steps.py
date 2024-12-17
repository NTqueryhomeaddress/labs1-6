from order_factory import PhysicalOrderFactory, DigitalOrderFactory
from behave import given, when, then

@given('a physical order factory')
def step_given_physical_factory(context):
    context.factory = PhysicalOrderFactory()

@given('a digital order factory')
def step_given_digital_factory(context):
    context.factory = DigitalOrderFactory()

@when('I create a physical order')
def step_when_create_physical(context):
    context.result = context.factory.create_order().process()

@when('I create a digital order')
def step_when_create_digital(context):
    context.result = context.factory.create_order().process()

@then('the result should be "{expected}"')
def step_then_result_should_be(context, expected):
    assert context.result == expected