Anexo 2: Respuestas a los problemas del curso
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _arrow_01:

Solution:: 

    import arrow

    today = arrow.now('Atlantic/Canary')
    future = today.shift(years=89, months=3, days=9)
    print(future.strftime("%A"))
