import { connect } from "react-redux"

function Footer(){
    return(
        <nav className="w-full py-3 bg-azul-marino-400 sticky top-[100vh]">
            <p className="text-gris-500 text-center text-white my-2">Oficina de Operaciones de Asistencia<br />Subdirección de Asistencia al Contribuyente</p>
        </nav>
    )
}

const mapStateToProp = state => ({

})

export default connect(mapStateToProp, {

}) (Footer)