import pytest
import jinja2
import os
import webbrowser
import dataclasses


@dataclasses.dataclass
class Error:
    title: str
    passed: bool
    failed: bool
    time: int
    message: str

def pytest_sessionstart(session):
    """Хук начала тестов"""
    session.results = dict()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук после каждого теста"""
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call':
        item.session.results[item] = result


def pytest_sessionfinish(session, exitstatus):
    """Хук финала тестов"""
    errors = []
    for value in session.results.values():
        errors.append(Error(
            passed=value.passed,
            failed=value.failed,
            title=value.head_line,
            time=round(value.duration, 2),
            message=((value.failed and value.longrepr.chain[0][1].message) or '')
        ))

    template = jinja2.Template("""\
    <title>{{ title }}</title>
    
    <table>
        <tr>
            <td><b>Название теста</b></td>
            <td><b>Результат</b></b></td>
            <td><b>Время</b></td>
            <td><b>Ошибка</b></td>
        </tr>
        {% for error in errors %}
            <tr>
                <td>{{ error.title }}</td>
                {% if error.passed %}
                    <td style="color: green;">Пройден</td>
                {% else %}
                    <td style="color: red;">Не пройден</td>
                {% endif %}
                <td>{{ error.time }} сек.</td>
                <td style="color: red;">{{ error.message }}</td>
            </tr>
        {% endfor %}
    </table>
    """)
    html = template.render(title="Результаты тестов", errors=errors)
    with open('results.html', 'w') as f:
        f.write(html)
        f.close()
    webbrowser.open(f'file:///{os.getcwd()}\\results.html')