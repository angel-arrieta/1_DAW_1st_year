var movimientos = [
    { tipo: 'Gasto', monto: 50, fecha: '2023-01-15', descripcion: 'Comida' },
    { tipo: 'Ingreso', monto: 100, fecha: '2023-02-10', descripcion: 'Salario' },
    { tipo: 'Gasto', monto: 30, fecha: '2023-03-05', descripcion: 'Transporte' },
    { tipo: 'Ingreso', monto: 200, fecha: '2023-04-20', descripcion: 'Venta' },
    { tipo: 'Gasto', monto: 80, fecha: '2023-05-12', descripcion: 'Ropa' },
    { tipo: 'Ingreso', monto: 150, fecha: '2023-06-08', descripcion: 'Regalo' }
  ];
var resultadoHTML = document.getElementById('resultado');
  
var tabla = document.createElement('table');
  
var encabezados = ['Tipo', 'Monto', 'Fecha', 'Descripción'];
var encabezadosRow = document.createElement('tr');
encabezados.forEach(function(encabezado) {
    var th = document.createElement('th');
    th.textContent = encabezado;
    encabezadosRow.appendChild(th);
  });
tabla.appendChild(encabezadosRow);
  
movimientos.forEach(function(movimiento) {
    var fila = document.createElement('tr');
  
    var tipoCelda = document.createElement('td');
    tipoCelda.textContent = movimiento.tipo;
    fila.appendChild(tipoCelda);
  
    var montoCelda = document.createElement('td');
    montoCelda.textContent = movimiento.monto;
    fila.appendChild(montoCelda);
  
    var fechaCelda = document.createElement('td');
    fechaCelda.textContent = movimiento.fecha;
    fila.appendChild(fechaCelda);
  
    var descripcionCelda = document.createElement('td');
    descripcionCelda.textContent = movimiento.descripcion;
    fila.appendChild(descripcionCelda);
  
    tabla.appendChild(fila);
  });
  
resultadoHTML.appendChild(tabla);
  