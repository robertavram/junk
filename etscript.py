

def country_currency_set():
    from django.db import connection
    from publics.models import Currency
    from users.models import Country
    usd = Currency.objects.get(code='USD')
    for c in Country.objects.exclude(name='Global').all():
        connection.set_tenant(Country.objects.get(name=c.name))
        if not c.local_currency:
            c.local_currency=usd
            c.save()


def local_country_keep():
    from users.models import Country
    c_names = ['Lebanon', 'Sudan', 'Global', 'UAT', 'Syria', 'Syria Cross Border',
               'Jordan', 'Pakistan', 'Palestine']
    deletable = Country.objects.exclude(name__in=c_names)

    assert Country.objects.filter(name__in=c_names).count() == len(c_names)

    deletable.delete()
