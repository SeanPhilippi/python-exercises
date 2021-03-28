export default class Pangram {
  private sentence: string;
  constructor(sentence: string) {
    this.sentence = sentence;
  }
  alphabet = 'abcdefghijklmnopqrstuvwxyz';

  isPangram = (): boolean | string => {
    const cleanedSentence = this.sentence.replace(/[^a-z]+/gi, '').toLowerCase().split('').sort().join('');
    const lettersString = [...new Set(cleanedSentence)].join('');
    if (lettersString == this.alphabet) {
      return true;
    } else {
      return false;
    }
  }
}