export class ResistorColor {
    private colors: string[]
    private hash: {
        [key: string]: number;
    }

    constructor(colors: string[]) {
        if (colors.length >= 2) {
            this.colors = colors;
        } else {
            throw new Error('At least two colors need to be present');
        }
            
        this.hash = {
            black: 0,
            brown: 1,
            red: 2,
            orange: 3,
            yellow: 4,
            green: 5,
            blue: 6,
            violet: 7,
            grey: 8,
            white: 9,
        }
    }

    value = (): number => {
      const nums: number[] = [];
      for (let i = 0; i < 2; i++) {
          nums.push(this.hash[this.colors[i]]);
      }
      const strNums = nums.map(String);
      return Number(strNums.join(''));
    }
}
