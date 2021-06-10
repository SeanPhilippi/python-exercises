

class Matrix {
  rows: number[];
  constructor(matrix: string) {
    const stringRows = matrix.split('\n');
    const rows = stringRows.map(str => str.split(' ')).map(Number);
    console.log('rows', rows)
    // const columns =
    // const columnCount = rows[0].length;
    this.rows = rows;
    // this.columns = columns;
  }
}

export default Matrix;