const fs = require('fs')
const JS2Py = require('js-to-py').JS2Py

const DIR = './node_modules/bfx-hf-indicators/lib'

const dirList = fs.readdirSync(DIR)
const js2py = new JS2Py()

dirList.map((name) => {
  const js = fs.readFileSync(`${DIR}/${name}`, { encoding: 'utf8'})
  try {
    const py = js2py.convert(js)
    const destPyFile = `bfxhfindicators/${name.replace('.js', '.py')}`
    fs.writeFileSync(destPyFile, py)
  } catch (ex) {
    console.log(`Error in ${name}:`, ex)
  }
})
