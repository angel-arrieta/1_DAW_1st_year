class Calcular (var primero: Int, var segundo: Int){
    fun mas(){
        var sumado = primero + segundo
        return sumado
    }
    fun menos(){
        var restado = primero - segundo
        return restado
    }
    fun por(){
        var multiplicado = primero * segundo
        return multiplicado
    }
    fun entre(){
        var dividido = primero / segundo
        return dividido
    }
}
fun main(varargs: Int){
    val num1 = readline()
    val num2 = readline()
    val operacion = Calcular(num1, num2)
    println(operacion.mas())
    println(operacion.menos())
    println(operacion.por())
    println(operacion.entre())
}