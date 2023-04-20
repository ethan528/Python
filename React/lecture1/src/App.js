import {Fragment} from 'react';

function App() {
  const a = 'react2'
  return (
    <Fragment>
      {/* {여기는 주석입니다} */}
      {a == 'react' ? (
        <h1>리액트입니다.</h1>
      ) : (
        <h1 style={{
          backgroundColor:"red",
          color:"green",
          fontSize:"48px"
        }}>리액트가 아닙니다.</h1>
      )}
    </Fragment>
  );
}

export default App;
