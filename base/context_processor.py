def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carroto"].items():
                total += float (value ["acumulado"])
    return { "total_carrito": total}