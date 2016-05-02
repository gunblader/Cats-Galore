var Title = React.createClass({
	propTypes: {
		title: React.PropTypes.string
	},

	render: function() {
		return (
			<h2>{this.props.title}s</h2>
			)
	}
})

var Desc = React.createClass({
	propTypes: {
		desc: React.PropTypes.string,
		isModel: React.PropTypes.bool
	},

	getDefaultProps: function() {
		return {
			desc: 'No Descroption'
		}
	},

	getInitialState: function() {
		return {
			value: 1
		}
	},

	componentDidMount: function() {
		this.setState({
			value: this.state.value + 19
		});
	},

	_addByOne: function() {
		this.setState({
			value: this.state.value + 1
		});
	},

	render: function() {
		var model = "N/A"
		if (this.props.isModel) {
			model = (<Model desc={this.props.desc} />)
		}

		return (
			<div>
			<p>Here, you can find a database of pet shelter <Model desc={this.props.desc} />s. Click on one to learn more about the <Model desc={this.props.desc} />!</p>
			{this.state.value} <br/>
			<button onClick={this._addByOne}>Click Me</button>
			</div>
			)
	}
})

var Model = React.createClass({
	propTypes: {
		desc: React.PropTypes.string
	},
	render: function() {
		return (
			<span>{this.props.desc}</span>
			)
	}
})

ReactDOM.render(
	<Title title="Organization" />,
	document.getElementById('head')
);
ReactDOM.render(
	<Desc desc="organization" isModel={true} />,
	document.getElementById('desc')
);