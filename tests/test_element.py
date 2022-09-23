from nicegui import ui

from .user import User


def test_classes(user: User):
    label = ui.label('Some label')

    def assert_classes(classes: str) -> None:
        assert user.selenium.find_element_by_xpath(f'//*[normalize-space(@class)="{classes}" and text()="Some label"]')

    user.open('/')
    assert_classes('')

    label.classes('one')
    assert_classes('one')

    label.classes('one')
    assert_classes('one')

    label.classes('two three')
    assert_classes('one two three')

    label.classes(remove='two')
    assert_classes('one three')

    label.classes(replace='four')
    assert_classes('four')


def test_style(user: User):
    label = ui.label('Some label')

    def assert_style(style: str) -> None:
        assert user.selenium.find_element_by_xpath(f'//*[normalize-space(@style)="{style}" and text()="Some label"]')

    user.open('/')
    assert_style('')

    label.style('color: red')
    assert_style('color: red;')

    label.style('color: red')
    assert_style('color: red;')

    label.style('color: blue')
    assert_style('color: blue;')

    label.style('font-weight: bold')
    assert_style('color: blue; font-weight: bold;')

    label.style(remove='color: blue')
    assert_style('font-weight: bold;')

    label.style(replace='text-decoration: underline')
    assert_style('text-decoration: underline;')


def test_props(user: User):
    input = ui.input()

    def assert_props(*props: str) -> None:
        class_conditions = [f'contains(@class, "q-field--{prop}")' for prop in props]
        assert user.selenium.find_element_by_xpath(f'//label[{" and ".join(class_conditions)}]')

    user.open('/')
    assert_props('standard', 'labeled')

    input.props('dark')
    assert_props('standard', 'labeled', 'dark')

    input.props('dark')
    assert_props('standard', 'labeled', 'dark')

    input.props(remove='dark')
    assert_props('standard', 'labeled')
