import pytest
from Mobile.createCustomer import EworkMobileTest as CreateCustomer
from Mobile.viewNewlyCustomer import EworkMobileTest as ViewCustomer
from Web.createNewCompany import EsuiteWebTest as CreateCompany

@pytest.mark.order(1)
def test_create_customer():
    """Membuat Data Customer Baru."""
    test = CreateCustomer()
    test.run_test()

@pytest.mark.order(2)
def test_view_new_customer():
    """Cek Data Customer Yang Baru Saja Dibuat."""
    test = ViewCustomer()
    test.run_test()

@pytest.mark.order(3)
def test_create_company():
    """Membuat Data Company Baru."""
    test = CreateCompany()
    test.run_test()
