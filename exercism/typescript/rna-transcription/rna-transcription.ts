class Transcriptor {
  private rnaHash: {
    [key: string]: string;
  }

  constructor() {
    this.rnaHash = {
      G: 'C',
      C: 'G',
      T: 'A',
      A: 'U',
    }
  }

  toRna = (dna: string): string => {
    const rnaArray: string[] = [];
    for (const letter of dna) {
      if (letter in this.rnaHash) {
        rnaArray.push(this.rnaHash[letter]);
      } else {
        throw new Error('Invalid input DNA.');
      }
    }
    return rnaArray.join('');
  }
}

export default Transcriptor
